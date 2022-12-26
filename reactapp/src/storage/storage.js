const put = (key, data) => {
  try {
    localStorage.setItem(key, data);
    return true;
  } catch (error) {
    console.log("Error storing the data of " + key, error);
    return false;
  }
};

const get = (key, defaultValue = null) => {
  try {
    let data = localStorage.getItem(key);
    if (data == null) {
      return defaultValue;
    }
    return data;
  } catch (error) {
    console.log("Error getting the data of " + key, error);
    return defaultValue;
  }
};

const remove = (key) => {
  try {
    localStorage.removeItem(key);
    return true;
  } catch (error) {
    console.log("Error removing the data of " + key, error);
    return false;
  }
};

export default { get, remove, put };
