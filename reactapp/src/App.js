import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import { Login } from "./Login";
import { Signup } from "./Signup";
import { ForgotPassword } from "./ForgotPassword";
import { Home } from "./Home";

function App() {
  const [currentForm, setCurrentForm] = useState("home");

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  };

  return (
    <div className="App">
      {currentForm == "home" && <Home onFormSwitch={toggleForm} />}
      {currentForm == "login" && <Login onFormSwitch={toggleForm} />}
      {currentForm == "signup" && <Signup onFormSwitch={toggleForm} />}
      {currentForm == "forgotpassword" && (
        <ForgotPassword onFormSwitch={toggleForm} />
      )}
    </div>
  );
}

export default App;
