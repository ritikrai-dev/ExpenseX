import express from "express";
import protect from "../middleware/authMiddleware.js";
import {
  getCategoryAnalytics,
  getMonthlyExpense,
} from "../controllers/analyticsController.js";

const router = express.Router();

router.get("/category", protect, getCategoryAnalytics);

router.get("/monthly-expense", protect, getMonthlyExpense);

export default router;