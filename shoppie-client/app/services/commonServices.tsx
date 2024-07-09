import { RegisterData } from "../interface"
import axiosInstance from "./interceptor"

export default async function register(data: RegisterData){
return await axiosInstance.post('customers/register',data)

}
