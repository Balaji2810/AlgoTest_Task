import { ToastContainer, toast } from "react-toastify";

import "react-toastify/dist/ReactToastify.css";

export const notify = (type, msg = "", autoClose = 2500) => {
  let theme = {
    position: "top-center",
    autoClose: autoClose,
    hideProgressBar: false,
    closeOnClick: true,
    pauseOnHover: true,
    draggable: true,
    progress: undefined,
    theme: "light",
  };
  switch (type) {
    case "info":
      toast.info(msg, theme);
      break;
    case "warning":
      toast.warning(msg, theme);
      break;
    case "error":
      toast.error(msg, theme);
      break;
    case "success":
      toast.success(msg, theme);
      break;
    default:
      toast(msg, theme);
  }
};

export const MyToastContainer = () => <ToastContainer />;
