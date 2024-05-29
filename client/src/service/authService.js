import axios from 'axios';
import UserService from '@/service/userService'

const baseUrl = "api/v1/user/"


class AuthService {
    login(user) {
        return axios
        .post(baseUrl + "login/", {
            email: user.email,
            password: user.password
        })
        .then(response => {
            if (response.data.access) {
                localStorage.setItem("token", JSON.stringify(response.data));
            }
            UserService.getUserProfile()

            return response.data;
        });
    }

    logout() {
        localStorage.removeItem("token");
    }

    register(user) {
        return axios
        .post(baseUrl + "register/", {
            email: user.email,
            password: user.password,
            password_confirm: user.password_confirm
        });
    }
}

export default new AuthService();