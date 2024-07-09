import axios from "axios";
// import serverConfig from "./serverConfig";
// import { refreshToken } from "./AdminServices";
import Swal from "sweetalert2";
import refreshToken from "./authServices";
const endPoint = process.env.NEXT_PUBLIC_API_URL
export const axiosInstance = axios.create({
  baseURL: `${endPoint}`,
  headers: {
    "Content-type": "application/json",
  },
});

axiosInstance.interceptors.request.use((request) => {
  const token = localStorage.getItem("AccessToken");
  const Rtoken = localStorage.getItem("refreshToken");

  if (token && Rtoken) {
    request.headers.Authorization = `Bearer ${token}`;
  } else {
    request.headers.Authorization = `Bearer ${Rtoken}`;
  }
  return request;
});

let isRefreshing = false;

axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const originalRequest = error.config;
    if (
      error.response.status === 401 &&
      !originalRequest._retry &&
      error.config.url !== "admin/refreshAccessToken"
    ) {
      if (!isRefreshing) {
        isRefreshing = true;
        try {
          const accessToken = await refreshAccessToken();

          axiosInstance.defaults.headers.common["Authorization"] = accessToken;
          originalRequest.headers["Authorization"] = accessToken;
          isRefreshing = false;
          return axiosInstance(originalRequest);
        } catch (error) {
          Swal.fire({
            title: "Token Expired",
            text: "Your session has expired. Please log in again.",
            icon: "warning",
            confirmButtonText: "OK",
            allowOutsideClick: false,
          }).then((result) => {
            if (result.isConfirmed) {
              localStorage.clear();
              window.location.replace("/login");
              return Promise.reject(error);
            }
          });
        }
      } else {
        isRefreshing = false;
      }
    }
    return Promise.reject(error);
  }
);

const refreshAccessToken = async () => {
  try {
    const res = await refreshToken();

    const accessToken = res.data.access_token;
    localStorage.setItem("AccessToken", accessToken);

    return accessToken;
  } catch (error) {
    throw new Error("Failed to refresh access token.");
  }
};