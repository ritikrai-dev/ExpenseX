import express from 'express';
import connectDB from "./config/db.js";
import pkg from 'dotenv';
const dotenv  = pkg;

dotenv.config();

connectDB();
const app = express();;
const PORT = process.env.PORT

app.listen(PORT,()=>{
    console.log(`Running on ${PORT}`)
})