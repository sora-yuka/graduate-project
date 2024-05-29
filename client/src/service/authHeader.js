import axios from 'axios';


const setup = (store) => {
    axios.interceptors.request.use(
        config => {
            const token = JSON.parse(localStorage.getItem("token"));

            if (token && token.access) {
                config.headers["Authorization"] = "Bearer " + token.access;
            }
            return config;
        },
        errors => {
            return Promise.reject(errors);
        }
    );

    axios.interceptors.request.use(
        response => {
            return response;
        },
        async errors => {
            const originalConfig = errors.config;

            if (errors.response) {
                if (errors.response.status === 401 && !originalConfig._retry) {
                    originalConfig._retry = true;

                    try {
                        const rs = await axios.post("http://localhost:8000/api/v1/token/refresh/", {
                            refresh: JSON.parse(localStorage.getItem("token")).refresh
                        });

                        const { access } = rs.data;
                        localStorage.setItem("token", JSON.stringify({
                            ...JSON.parse(localStorage.getItem("token")),
                            access: access,
                        }));

                        axios.defaults.headers.common["Authorization"] = "Bearer " + access;
                        return axios(originalConfig);
                    } catch (_error) {
                        return Promise.reject(_error);
                    }
                }
            }
            return Promise.reject(_error)
        }
    )
}

export default setup;