import React, { useState } from "react";
import POST from "./api/POST";

import helper from "./helper";
import { notify, MyToastContainer } from "./Toast";

export const Signup = (props) => {
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");
  const [pass2, setPass2] = useState("");
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [phoneOtp, setPhoneOtp] = useState("");
  const [emailOtp, setEmailOtp] = useState("");
  const [phoneOtpBtn, setPhoneOtpBtn] = useState(false);
  const [emailOtpBtn, setEmailOtpBtn] = useState(false);

  const handleSubmit = () => {
    if (
      email.length == 0 ||
      pass.length == 0 ||
      pass2.length == 0 ||
      name.length == 0 ||
      phone.length == 0 ||
      email.length == 0 ||
      phoneOtp.length == 0 ||
      emailOtp.length == 0
    ) {
      notify("warning", "Empty Inputs!!");
      return;
    }
    if (name.length < 3) {
      notify("warning", "Check the Name, minimum 3 characters!!");
      return;
    }

    if (!/^[a-zA-Z]+$/.test(name)) {
      notify("warning", "Check the Name!");
      return;
    }

    let re = /^([\w\.\-]+)@([\w\-]+)((\.(\w){2,63}){1,3})$/;
    if (!re.test(email)) {
      notify("warning", "Check the Email!");
      return;
    }
    re = /^[6-9]\d{9}$/;
    if (!re.test(phone)) {
      notify("warning", "Check the phone number!");
      return;
    }
    if (pass.length < 6 || pass.length > 16) {
      notify(
        "warning",
        "Check the password, minimum 6 characters 16 maximum!!"
      );
      return;
    }
    if (pass != pass2) {
      notify("warning", "Password doesn't match!");
      return;
    }
    console.log("resData");
    POST.signup(
      email.trim(),
      phone.trim(),
      emailOtp.trim(),
      phoneOtp.trim(),
      name.trim(),
      pass
    )
      .then((res) => res)
      .then((resData) => {
        if (resData.ok) {
          notify("success", "User Created!!");
          setEmail("");
          setName("");
          setEmailOtp("");
          setPhone("");
          setPhoneOtp("");
          setPass("");
          setPass2("");
          setEmailOtpBtn(false);
          setPhoneOtpBtn(false);
        } else {
          switch (resData.data.type) {
            case "Email":
              notify("error", "Email already present!!");
              break;
            case "Phone":
              notify("error", "Phone already present!!");
              break;
            case "otp":
              notify("error", "Incorrect OTP!!");
              setPhoneOtp("");
              setEmailOtp("");
              setEmailOtpBtn(false);
              setPhoneOtpBtn(false);
              break;
          }
        }
      });
  };

  return (
    <div className="auth-form-container">
      <MyToastContainer />
      <h2>SignUp</h2>
      <div className="signup-form">
        <label htmlFor="name">name</label>
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          name="name"
          id="name"
          placeholder="full name"
        />
        <label htmlFor="email">email</label>
        <div>
          <input
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="youremail@gmail.com"
            id="email"
            name="email"
          />
          <button
            className="sent_otp"
            onClick={() => {
              let re = /^([\w\.\-]+)@([\w\-]+)((\.(\w){2,63}){1,3})$/;
              if (!re.test(email)) {
                notify("warning", "Check the Email!");
              } else {
                setEmailOtpBtn(true);
                helper.send_otp_email(email, notify);
              }
            }}
          >
            send OTP
          </button>
        </div>
        {emailOtpBtn && (
          <>
            <label htmlFor="otp">email OTP</label>
            <input
              value={emailOtp}
              onChange={(e) => setEmailOtp(e.target.value.replace(/\D/, ""))}
              placeholder="Enter Email OTP"
              id="otp"
              name="otp"
              max="6"
            />
          </>
        )}
        <label htmlFor="phone">phone</label>
        <div>
          <input
            value={phone}
            onChange={(e) => setPhone(e.target.value.replace(/\D/, ""))}
            placeholder="phone number"
            id="phone"
            name="phone"
          />
          <button
            className="sent_otp"
            onClick={() => {
              let re = /^[6-9]\d{9}$/;
              if (!re.test(phone)) {
                notify("warning", "Check the phone number!");
                return;
              } else {
                setPhoneOtpBtn(true);
                helper.send_otp_sms(phone, notify);
              }
            }}
          >
            send OTP
          </button>
        </div>
        {phoneOtpBtn && (
          <>
            <label htmlFor="phone_otp">phone OTP</label>
            <input
              value={phoneOtp}
              onChange={(e) => setPhoneOtp(e.target.value.replace(/\D/, ""))}
              placeholder="Enter Phone OTP"
              id="phone_otp"
              name="phone_otp"
            />
          </>
        )}
        <label htmlFor="password">password</label>
        <input
          value={pass}
          onChange={(e) => setPass(e.target.value)}
          type="password"
          placeholder="6 to 16 Characters"
          id="password"
          name="password"
        />
        <label htmlFor="password2">confirm password</label>
        <input
          value={pass2}
          onChange={(e) => setPass2(e.target.value)}
          type="password"
          placeholder="********"
          id="password2"
          name="password2"
        />
        {phoneOtpBtn && emailOtpBtn && (
          <button onClick={() => handleSubmit()}>SignUp</button>
        )}
      </div>
      <button className="link-btn" onClick={() => props.onFormSwitch("login")}>
        Already have an account? Login here.
      </button>
    </div>
  );
};
