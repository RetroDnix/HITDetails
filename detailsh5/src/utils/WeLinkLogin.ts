import { axiosInstance } from "@/utils/Axios";

export const ProxyLogin = async (AuthCode: string) => {
  try {
    const params = new URLSearchParams();
    params.append('AuthCode', AuthCode);
    const response = await axiosInstance.post("/LoginProxy", params);
    console.log(response);
    return response.data
  }
  catch (error) {
      console.log(error);
      return "err"
  }
}

// export const getUserID = async (access_token: string, authCode: string) => {
//   const axiosConfig: AxiosRequestConfig = {
//     baseURL: 'https://open.welink.huaweicloud.com/api/auth/v2/userid', // api的base URL
//     timeout: 5000, // 设置请求超时时间
//     responseType: 'json',
//     withCredentials: true, // 是否允许带cookie这些
//     headers: {
//       'Content-Type': 'application/x-www-form-urlencoded',
//       'Access-Control-Allow-Origin': '*',
//       "x-wlk-Authorization": access_token
//     },
//     params: {code: authCode}
//   };
//   const axiosInstance = axios.create(axiosConfig);
//   try {
//     const response = await axiosInstance.get('');
//     return response.data.userId
//   }
//   catch (error) {
//       console.log(error);
//       return "err"
//   }
// }
