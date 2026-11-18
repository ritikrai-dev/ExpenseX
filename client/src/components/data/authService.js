import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:5000";

// Dedicated axios instance for Auth requests
const authClient = axios.create({
  baseURL: `${API_BASE}/api/auth`,
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 12000,
});

/**
 * Standardize error responses into human-friendly messages
 */
function normalizeError(error) {
  if (error.response) {
    // Server responded with non-2xx status
    const data = error.response.data;
    if (typeof data === "string") return data;
    if (data?.message) return data.message;
    if (data?.error) return data.error;
    return `Server error (${error.response.status}). Please try again.`;
  }
  if (error.request) {
    // Request was made but no response received (server down or CORS issue)
    return "Unable to connect to the server. Please check your internet connection or try again later.";
  }
  return error.message || "An unexpected error occurred.";
}

/**
 * Login user with email & password
 * @param {{ email: string, password: string }} credentials
 * @returns {Promise<{ success: boolean, token: string, user: object, message?: string }>}
 */
export async function loginUser(credentials) {
  try {
    const payload = {
      email: credentials.email.trim().toLowerCase(),
      password: credentials.password,
    };
    const response = await authClient.post("/login", payload);
    const data = response.data;

    // Guard against backends that return HTTP 200 with error messages
    if (!data.token) {
      throw new Error(data.message || "Invalid credentials provided.");
    }

    return data;
  } catch (error) {
    throw new Error(normalizeError(error), { cause: error });
  }
}

/**
 * Register / Signup user with name, email & password
 * Supports both /signup and /register backend routes
 * @param {{ name: string, email: string, password: string }} userData
 * @returns {Promise<{ success: boolean, token: string, user: object, message?: string }>}
 */
export async function signupUser(userData) {
  const payload = {
    name: userData.name.trim(),
    email: userData.email.trim().toLowerCase(),
    password: userData.password,
  };

  try {
    // Attempt /signup first; fall back to /register if 404
    let response;
    try {
      response = await authClient.post("/signup", payload);
    } catch (err) {
      if (err.response && err.response.status === 404) {
        response = await authClient.post("/register", payload);
      } else {
        throw err;
      }
    }

    const data = response.data;
    if (!data.token) {
      throw new Error(data.message || "Failed to create account.");
    }

    return data;
  } catch (error) {
    throw new Error(normalizeError(error), { cause: error });
  }
}
