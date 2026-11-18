import { useEffect, useState } from "react";
import "../style/setting.css";
import { toast } from "react-toastify";
import {
  getUser,
  updateUser,
  changePassword,
  isDemo,
} from "../components/data/dataService";

export default function Settings() {
  const [user, setUser] = useState({
    name: "",
    email: "",
  });

  const [passwords, setPasswords] = useState({
    currentPassword: "",
    newPassword: "",
    confirmPassword: "",
  });

  const [loading, setLoading] = useState(true);
  const demoActive = isDemo();

  useEffect(() => {
    fetchProfile();
  }, []);

  async function fetchProfile() {
    try {
      setLoading(true);
      const userData = await getUser();
      if (userData) {
        setUser({
          name: userData.name || "Guest User",
          email: userData.email || "guest@expensex.local",
        });
      }
    } catch (err) {
      console.error(err);
      toast.error("Failed to fetch profile");
    } finally {
      setLoading(false);
    }
  }

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const data = await updateUser(user);
      if (data?.success || data?.user) {
        toast.success(data?.message || "Profile updated successfully");
      } else {
        toast.error(data?.message || "Failed to update profile");
      }
    } catch (err) {
      console.error(err);
      toast.error("Failed to update profile");
    }
  }

  async function handlePasswordUpdate(e) {
    e.preventDefault();

    if (passwords.newPassword !== passwords.confirmPassword) {
      toast.error("New passwords do not match!");
      return;
    }

    try {
      const data = await changePassword(passwords);
      if (data?.success) {
        toast.success(data.message || "Password updated successfully");
        setPasswords({
          currentPassword: "",
          newPassword: "",
          confirmPassword: "",
        });
      } else {
        toast.error(data?.message || "Failed to change password");
      }
    } catch (err) {
      console.error(err);
      toast.error("Failed to change password");
    }
  }

  if (loading) {
    return <h2>Loading settings...</h2>;
  }

  return (
    <div className="settings-page">
      {demoActive && (
        <div
          style={{
            background: "#eff6ff",
            border: "1px solid #bfdbfe",
            color: "#1e40af",
            padding: "1rem",
            borderRadius: "8px",
            marginBottom: "1.5rem",
          }}
        >
          ℹ️ <strong>Guest Mode:</strong> You are browsing as a guest. Profile and
          preferences are stored locally on your device. Create an account to sync
          your profile across devices!
        </div>
      )}

      <form className="settings-form" onSubmit={handleSubmit}>
        <div className="profile-preview">
          <img
            src={`https://ui-avatars.com/api/?name=${encodeURIComponent(
              user.name || "Guest"
            )}&background=3b82f6&color=fff`}
            alt="profile"
          />
          <h2>Profile Settings</h2>
        </div>

        <div className="form-group">
          <label>Full Name</label>
          <input
            type="text"
            value={user.name}
            onChange={(e) =>
              setUser({
                ...user,
                name: e.target.value,
              })
            }
            required
          />
        </div>

        <div className="form-group">
          <label>Email Address</label>
          <input
            type="email"
            value={user.email}
            onChange={(e) =>
              setUser({
                ...user,
                email: e.target.value,
              })
            }
            required
          />
        </div>

        <button type="submit" className="primary-btn">
          Save Changes
        </button>
      </form>

      <form className="settings-form" onSubmit={handlePasswordUpdate}>
        <h2>🔒 Change Password</h2>

        <div className="form-group">
          <label>Current Password</label>
          <input
            type="password"
            placeholder="Current Password"
            value={passwords.currentPassword}
            onChange={(e) =>
              setPasswords({
                ...passwords,
                currentPassword: e.target.value,
              })
            }
            required
          />
        </div>

        <div className="form-group">
          <label>New Password</label>
          <input
            type="password"
            placeholder="New Password"
            value={passwords.newPassword}
            onChange={(e) =>
              setPasswords({
                ...passwords,
                newPassword: e.target.value,
              })
            }
            required
          />
        </div>

        <div className="form-group">
          <label>Confirm New Password</label>
          <input
            type="password"
            placeholder="Confirm Password"
            value={passwords.confirmPassword}
            onChange={(e) =>
              setPasswords({
                ...passwords,
                confirmPassword: e.target.value,
              })
            }
            required
          />
        </div>

        <button type="submit" className="primary-btn">
          Update Password
        </button>
      </form>
    </div>
  );
}