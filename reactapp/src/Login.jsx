import React, { useState } from "react";

import POST from "./api/POST";
import { notify, MyToastContainer } from "./Toast";
import storage from "./storage/storage";

export const Login = (props) => {
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");

  const handleSubmit = () => {
    POST.login(email, pass)
      .then((res) => res.data)
      .then((resData) => {
        if (resData.code == 200) {
          storage.put("refresh", resData.data.refresh);
          props.onFormSwitch("home");
        } else {
          notify("error", "Invalid ");
        }
      });
  };

  return (
    <div className="auth-form-container">
      <MyToastContainer />
      <h2>Login</h2>
      <div className="login-form">
        <label htmlFor="email_or_phone">email or phone</label>
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="youremail@gmail.com | 9087715463"
          id="email_or_phone"
          name="email_or_phone"
        />
        <label htmlFor="password">password</label>
        <input
          value={pass}
          onChange={(e) => setPass(e.target.value)}
          type="password"
          placeholder="********"
          id="password"
          name="password"
        />
        <button
          className="link-btn"
          onClick={() => props.onFormSwitch("forgotpassword")}
        >
          Forgot Password? click here.
        </button>
        <button onClick={() => handleSubmit()}>Log In</button>
      </div>
      <button className="link-btn" onClick={() => props.onFormSwitch("signup")}>
        Don't have an account? SignUp here.
      </button>
    </div>
  );
};
