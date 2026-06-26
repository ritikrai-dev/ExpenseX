import express from "express";
import { registerUser , login } from "../controllers/authControllers.js";

const routes = express.Router()

routes.post("/register",registerUser);
routes.post("/login",login);
export default routes;