import express from "express";
import { addTransaction , getTransactions , getTransactionById , updateTransaction , deleteTransaction} from "../controllers/transactionController.js";
import protect from "../middleware/authMiddleware.js";
const routes = express.Router()

routes.post("/", protect, addTransaction);
routes.get("/", protect, getTransactions);
routes.get("/:id", protect, getTransactionById);
routes.put("/:id", protect, updateTransaction);
routes.delete("/:id", protect, deleteTransaction);


export default routes;