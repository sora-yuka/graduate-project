import { createStore } from "vuex";

export default createStore({
    state: {
        token: JSON.parse(localStorage.getItem("token"))?.access || null
    },
    getters: {
        isAuthenticated: state => !!state.token
    },
    mutations: {
        setToken(state, token) {
            state.token = token
            localStorage.setItem("token", JSON.stringify({ access: token }))
        },
        clearToken(state) {
            state.token = ""
            localStorage.removeItem("token")
        },
    },
    actions: {
        login({ commit }, token) {
            commit("setToken", token)
        },
        logout({ commit }) {
            commit("clearToken")
        }
    },
    modules: {
        
    }
})