import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    chunkSizeWarningLimit: 2000, // Aumenta este número según tus necesidades
  },
  server:{
    host:"0.0.0.0",
  },
  plugins: [react()],
})
