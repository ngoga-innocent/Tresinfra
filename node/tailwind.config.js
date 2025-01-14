/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./../**/*.{html,js,py}"],
  theme: {
    extend: {
      color:{
        'primary':'#dc2626',
        'sky':'#0c4a6e',
        'semi_sky':'#0369a1'
      }
    },
  },
  plugins: [],
}

