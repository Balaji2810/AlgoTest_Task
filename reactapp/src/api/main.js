import { create } from "apisauce";

export const apiClient = create({
  baseURL: "http://localhost:5000/api",
});
