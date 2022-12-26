import POST from "./api/POST";
import storage from "./storage/storage";
import { notify } from "./Toast";

const send_otp_sms = (phone, toast, cancelToken) => {
  let re = /^[6-9]\d{9}$/;
  if (re.test(phone)) {
    notify("info", "Checking Phone!!", 1000);
    POST.check(phone)
      .then((res) => res.data)
      .then((resData) => {
        if (!resData.data.user_present) {
          notify("info", "Sending OTP!!", 1500);
          POST.send_otp_sms(phone, cancelToken)
            .then((res) => res.data)
            .then((resData) => {
              if (resData.data.otp_sent) {
                notify("success", "OTP Sent!!");
              }
            });
        } else {
          notify("warning", "Email already exist in the database!!");
        }
      });
  } else {
    toast("warning", "Check The Phone Number!");
  }
};

const send_otp_email = (email, toast, cancelToken = null) => {
  let re = /^([\w\.\-]+)@([\w\-]+)((\.(\w){2,63}){1,3})$/;
  if (re.test(email)) {
    notify("info", "Checking Email!!", 1000);
    POST.check(email)
      .then((res) => res.data)
      .then((resData) => {
        if (!resData.data.user_present) {
          notify("info", "Sending OTP!!");
          POST.send_otp_email(email, cancelToken)
            .then((res) => res.data)
            .then((resData) => {
              if (resData.data.otp_sent) {
                notify("success", "OTP Sent!!");
              }
            });
        } else {
          notify("warning", "Email already exist in the database!!");
        }
      });
  } else {
    toast("warning", "Check The Email!");
  }
};

const access = async () => {
  try {
    let res = await POST.access();
    let resData = res.data;
    if (resData.code == 200) {
      storage.put("access", resData.data.access);
      return true;
    } else {
      return false;
    }
  } catch {
    return false;
  }
};

export default {
  send_otp_email,
  send_otp_sms,
  access,
};
