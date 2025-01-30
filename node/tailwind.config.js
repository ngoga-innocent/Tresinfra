/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./../**/*.{html,js,py}"],
  theme: {
    extend: {
      colors:{
        'primary':'#dc2626',
        'sky':'#0c4a6e',
        'semi_sky':'#0369a1',
        'my_orange':'#F74E00',
        'heading':'#253746'
      }
    },
  },
  plugins: [],
}

