import express from 'express';
import connectDB from "./config/db.js";
import pkg from 'dotenv';
import User from './models/User.js';
import authRoutes from './routes/authRoutes.js';
import Transaction from './models/Transaction.js';
import transactionRoutes from "./routes/transactionRoutes.js";
import dashboardRoutes from "./routes/dashboardRoutes.js";
import analyticsRoutes from "./routes/analyticsRoutes.js";

import cors from "cors";
const dotenv  = pkg;

dotenv.config();
connectDB();
const users = await User.find();
console.log(users);
const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors({
    origin: "http://localhost:5173",
    methods: ["GET", "POST", "PUT", "DELETE"],
    credentials: true
}));


app.use('/api/auth',authRoutes);
app.use("/api/transactions", transactionRoutes);
app.use("/api/dashboard", dashboardRoutes);
app.use("/api/analytics", analyticsRoutes);

const PORT = process.env.PORT

app.listen(PORT,()=>{
    console.log(`Running on ${PORT}`)
})