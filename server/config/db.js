import mongoose from "mongoose";

const connectDB = async ()=>{
    try{
        const conn = await mongoose.connect(process.env.MONGODB);
        console.log("DB Connected");
    }catch(error){
        console.error("Can't Connection :",error.message);
    }
};

export default connectDB;