import express from 'express';
import connectDB from "./config/db.js";
import pkg from 'dotenv';
import User from './models/User.js';
import authRoutes from './routes/authRoutes.js'
const dotenv  = pkg;

dotenv.config();
connectDB();
const users = await User.find();
console.log(users);
const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


app.use('/api/auth',authRoutes)
const PORT = process.env.PORT

app.listen(PORT,()=>{
    console.log(`Running on ${PORT}`)
})