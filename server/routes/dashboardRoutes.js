import express from "express";
import { getDashboard } from "../controllers/dashboardController.js";
import protect from "../middleware/authMiddleware.js";

const routes = express.Router();

routes.get("/", protect, getDashboard);

export default routes;