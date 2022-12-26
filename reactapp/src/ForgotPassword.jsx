import React, { useState } from "react";

import { notify, MyToastContainer } from "./Toast";

export const ForgotPassword = (props) => {
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");
  const [otp, setOtp] = useState("");
  const [pass2, setPass2] = useState("");
  const [otpBtn, setOtpBtn] = useState(false);
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(email);
  };

  return (
    <div className="auth-form-container">
      <h2>Forgot Password</h2>
      <form className="login-form" onSubmit={handleSubmit}>
        <label htmlFor="email_or_phone">email or phone</label>
        <div>
          <input
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            type="email_or_phone"
            placeholder="youremail@gmail.com | 9087715463"
            id="email_or_phone"
            name="email_or_phone"
          />
          <button
            className="sent_otp"
            onClick={() => {
              // setOtpBtn(true)
              notify("success", "all ok here!!");
            }}
          >
            send OTP
          </button>
        </div>
        {otpBtn && (
          <>
            <label htmlFor="otp">OTP</label>
            <input
              value={otp}
              onChange={(e) => {
                setOtp(e.target.value);
              }}
              placeholder="Enter OTP"
              id="otp"
              name="otp"
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
          type="password2"
          placeholder="********"
          id="password2"
          name="password2"
        />
        {otpBtn && <button type="submit">Reset</button>}
      </form>
      <button className="link-btn" onClick={() => props.onFormSwitch("login")}>
        Click here to go Back to login form
      </button>
      <MyToastContainer />
    </div>
  );
};
