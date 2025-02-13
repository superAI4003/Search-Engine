import path from "path"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"
 
export default defineConfig({
  server: {
    host: '0.0.0.0', // Listen on all network interfaces
    port: 3000,      // Ensure this port is open in your firewall
  },
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})