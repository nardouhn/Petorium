// src/components/Navbar.jsx
import { PawPrint } from "lucide-react";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <header className="w-full bg-white shadow-sm fixed top-0 left-0 z-50">
      <div className="max-w-7xl mx-auto flex justify-between items-center py-4 px-6 border-b border-teal-100">
        {/* Logo */}
        <div className="flex items-center space-x-2">
          <div className="bg-[linear-gradient(90deg,#14B8A6_0%,#0EA5E9_100%)] p-2 rounded-full">
            <PawPrint className="text-[#D7F5F3] w-5 h-5" />
          </div>
          <a href="/" className="font-bold text-xl text-[#0D9488]">
            Petorium Vet Clinic
          </a>
        </div>

        {/* Menu */}
        <nav className="hidden md:flex space-x-8 text-gray-600 font-medium">
          <a href="/#about" className="hover:text-[#0891B2] transition-colors">
            About
          </a>
          <a
            href="#services"
            className="hover:text-[#0891B2] transition-colors"
          >
            Services
          </a>
          <a href="#book" className="hover:text-[#0891B2] transition-colors">
            Book Now
          </a>

          <a href="/signup" className="hover:text-[#0891B2] transition-colors">
            Login/ Sign up
          </a>
        </nav>
      </div>
      <div className="border-b border-[#7DE2D1]"></div>
    </header>
  );
}
