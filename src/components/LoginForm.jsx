import { PawPrint } from "lucide-react";

export default function LoginForm() {
  return (
    <div className="bg-white/70 backdrop-blur-xl rounded-2xl border border-teal-200 shadow-xl p-8 max-w-md w-full">
      <div className="space-y-6">
        <div>
          <label className="text-sm font-medium">Email *</label>
          <input
            type="email"
            className="mt-1 w-full rounded-xl border px-4 py-3 bg-teal-100/60 focus:outline-none focus:ring-2 focus:ring-teal-300"
          />
        </div>

        <div>
          <label className="text-sm font-medium">Mật khẩu (Password) *</label>
          <input
            type="password"
            className="mt-1 w-full rounded-xl border px-4 py-3 focus:outline-none focus:ring-2 focus:ring-teal-300"
          />
        </div>
      </div>

      <button className="mt-8 w-full rounded-xl bg-[linear-gradient(135deg,#75C7BE_0%,#3B7798_47%,#87EBE0_100%)] py-3 text-white font-semibold flex items-center justify-center gap-2">
        Đăng nhập (Log in)
        <PawPrint className="w-5 h-5" />
      </button>
    </div>
  );
}
