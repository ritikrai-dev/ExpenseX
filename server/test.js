import mongoose from "mongoose";
import dotenv from "dotenv";

dotenv.config();

try {
  console.log("URI:", process.env.MONGODB);

  const conn = await mongoose.connect(process.env.MONGODB);

  console.log("Connected!");
  console.log(conn.connection.host);
} catch (err) {
  console.error(err);
}

process.exit();

import mongoose from "mongoose";
import dotenv from "dotenv";

dotenv.config();

try {
  console.log("URI:", process.env.MONGODB);

  const conn = await mongoose.connect(process.env.MONGODB);

  console.log("Connected!");
  console.log(conn.connection.host);
} catch (err) {
  console.error(err);
}

process.exit();

import mongoose from "mongoose";
import dotenv from "dotenv";

dotenv.config();

try {
  console.log("URI:", process.env.MONGODB);

  const conn = await mongoose.connect(process.env.MONGODB);

  console.log("Connected!");
  console.log(conn.connection.host);
} catch (err) {
  console.error(err);
}

process.exit();