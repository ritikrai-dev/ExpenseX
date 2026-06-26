import jwt, { decode } from 'jsonwebtoken';
import User from '../models/User.js';

const protect = async (req,res,next) =>{
    try {
        if (req.headers.authorization && req.headers.authorization.startWith("Bearer")){
            const token = req.headers.authorization.split(" ")[1];
        }

        if(!token){
            return res.json({
                message:"Not authorized"
            });
        };

        const decoded = jwt.verify(token,process.env.JWT_SECRET);

        req.user = await User.findById(decoded.id).select("-password")//remove password for security purpose ;
        next();

    } catch (error) {
        res.json({
            message:error.message
        });
    };
};

export default protect;
