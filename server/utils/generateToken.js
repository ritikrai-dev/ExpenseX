import jwt from 'jsonwebtoken';

const generateToken = (userid) =>{
    return jwt.sign({id:userid},process.env.JWT_SECRET,{
        expiresIn:process.env.JWT_EXPIRES
    });
};

export default generateToken;