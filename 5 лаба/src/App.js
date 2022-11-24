import './App.css';
import { BrowserRouter, Route, Link, Routes } from "react-router-dom";
import React from "react";
import Rent from './Rent';
import Car from './Car';
import Cars from './Cars';


function App() {
    return (

        <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Rent />} />
                    <Route path="/rent" element={<Rent/>}/>
                    <Route path={`/rent/:pk`} element={<Car/>}>
                    <Route path="*" element={<p>Path not resolved</p>} /></Route>
                </Routes>
        </BrowserRouter>


    );
}

export default App;

