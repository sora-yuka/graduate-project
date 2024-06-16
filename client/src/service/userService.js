import axios from 'axios';


class UserService {
    getUserProfile() {
        const token = JSON.parse(localStorage.getItem("token"));

        return axios.get("http://localhost:8000/api/v1/profiles/me/", {
            headers: {
                "Authorization": "Bearer " + token.access
            }
        })
        .then(response => {
            localStorage.setItem("user", JSON.stringify(response.data))
            console.log("TOKEN: ", token)
        })
    }
}

export default new UserService();