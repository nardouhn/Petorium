import React from "react";

import { Toaster } from "sonner";
import { BrowserRouter, Routes, Route } from "react-router";
import ScrollToHash from "@/utils/ScrollToHash";
import HomePage from "@/pages/HomePage";
import NotFound from "@/pages/NotFound";
import SignupPage from "@/pages/SignupPage";
import LoginPage from "@/pages/LoginPage";
import ServicePage from "@/pages/ServicePage";
function App() {
  return (
    <>
      <Toaster richColors />

      <BrowserRouter>
        <ScrollToHash />
        <Routes>
          <Route path="/" element={<HomePage />} />

          <Route path="/signup" element={<SignupPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/services/:slug" element={<ServicePage />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
