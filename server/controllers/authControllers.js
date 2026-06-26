import bcrypt from 'bcrypt';
import User from '../models/User.js';
import generateToken from '../utils/generateToken.js';
// Register User
export const registerUser = async (req,res) =>{
    try {
        const { name, email, password } = req.body;
        const existingUser = await User.findOne({email});

        if(existingUser){
            return res.json({
                message :"Already Registered" 
            });
        };

        const hashPassword = await bcrypt.hash(password,10);

        const user = await User.create({
            name,
            email,
            password:hashPassword
        });

        const token = generateToken(user._id);
        res.json({
            success:true,
            token,
            user:{
                id : user._id,
                name:user.name,
                email:user.email
            }
        });
    } catch (error) {
        res.json({
            message:error.message
        });
    };
};

// Login User
export const login = async (req,res) =>{
    try {
        const {email,password} = req.body;
        const user = await User.findOne({email});
        if(!user){
            return res.json({
                message:"Invalid"
            });
        };

        const isMatch = await bcrypt.compare(password,user.password);

        if(!isMatch){
            return res.json({
                message:"Invalid Password"
            });
        };

        const token = generateToken(user._id);
        res.json({
            message:"Login Success",
            token,
            user:{
                id:user._id,
                name:user.name,
                email:user.email
            }
        });
    } catch (error) {
        res.json({
            message:error.message
        })
    }
}

