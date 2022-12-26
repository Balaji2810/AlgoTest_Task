import { apiClient } from "./main";
import storage from "../storage/storage";

const send_otp_sms = async (phone, cancelToken = null) => {
  let formdata = new FormData();
  formdata.append("phone", phone);
  return await apiClient.post("/v1/otp/phone", formdata, {
    headers: {},
    cancelToken,
  });
};

const send_otp_email = async (email, cancelToken = null) => {
  let formdata = new FormData();
  formdata.append("email", email);
  return await apiClient.post("/v1/otp/email", formdata, {
    headers: {},
    cancelToken,
  });
};

const check = async (phone_or_email, cancelToken = null) => {
  let formdata = new FormData();
  formdata.append("phone_or_email", phone_or_email);
  return await apiClient.post("/v1/user/check", formdata, {
    headers: {},
    cancelToken,
  });
};

const signup = async (
  email,
  phone,
  email_otp,
  phone_otp,
  name,
  password,
  cancelToken = null
) => {
  let formdata = new FormData();
  formdata.append("email", email);
  formdata.append("phone", phone);
  formdata.append("email_otp", email_otp);
  formdata.append("phone_otp", phone_otp);
  formdata.append("name", name);
  formdata.append("password", password);
  return await apiClient.post("/v1/user/signup", formdata, {
    headers: {},
    cancelToken,
  });
};

const login = async (phone_or_email, pass, cancelToken = null) => {
  let formdata = new FormData();
  formdata.append("phone_or_email", phone_or_email);
  formdata.append("password", pass);

  return await apiClient.post("/v1/token/refresh", formdata, {
    headers: {},
    cancelToken,
  });
};

const access = async (cancelToken = null) => {
  return await apiClient.post(
    "/v1/token/access",
    {},
    {
      headers: { Authorization: "Bearer " + storage.get("refresh") },
      cancelToken,
    }
  );
};

export default {
  send_otp_email,
  send_otp_sms,
  check,
  signup,
  login,
  access,
};
