import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import Login from './Login/Login.jsx'
import SignUP from './Login/SignUp.jsx'
import './index.css'
import {createBrowserRouter , RouterProvider} from 'react-router-dom'
import Start from './Start.jsx'

const router = createBrowserRouter([
  {
    path:'/',
    element:<Start />,

  },
  {
    path:'/Login',
    element:<Login />,

  },
  {
    path:'/SignUp',
    element:<SignUP/>,

  },
  {
    path:'/App/:Username/:Chat',
    element:<App/>,

  }
  

])

createRoot(document.getElementById('root')).render(
  //<StrictMode>
    <RouterProvider router={router}/>
  //</StrictMode>,
)
