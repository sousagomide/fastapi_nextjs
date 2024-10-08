"use client";

import { useContext, useState } from "react";
import AuthContext from "../context/AuthContext";
import axios from "axios";

const Login = () => {
    const { login } = useContext(AuthContext);
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [registerUsername, setRegisterUsername] = useState("");
    const [registerPassword, setRegisterPassword] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        login(username, password);
    };

    const handleRegister = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://localhost:8000/auth/register", {
               username: registerUsername,
               password: registerPassword 
            });
            login(registerUsername, registerPassword);
        } catch (error) {
            console.error("Registration failed", error);
        }
    }

    return (
        <div className="container">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="username" className="form-label">Username</label>
                    <input type="text" className="form-control" id="username" value={username} onChange={(e) => setUsername(e.target.value)} />
                </div>
                <div className="mb-3">
                    <label htmlFor="password" className="form-label">Password</label>
                    <input type="password" className="form-control" id="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                </div>
                <button type="submit" className="btn btn-primary">Login</button>
            </form>

            <h2>Register</h2>
            <form onSubmit={handleRegister}>
                <div className="mb-3">
                    <label htmlFor="registerUsername" className="form-label">Username</label>
                    <input type="text" className="form-control" id="registerUsername" value={registerUsername} onChange={(e) => setRegisterUsername(e.target.value)} />
                </div>
                <div className="mb-3">
                    <label htmlFor="registerPassword" className="form-label">Password</label>
                    <input type="password" className="form-control" id="registerPassword" value={registerPassword} onChange={(e) => setRegisterPassword(e.target.value)} />
                </div>
                <button type="submit" className="btn btn-primary">Registrar</button>
            </form>
        </div>
    );
};

export default Login;
