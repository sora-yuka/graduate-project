<template>
    <div class="app">
        <nav class="nav">
        <div class="container">
            <router-link to="/"><span class="home-button">COURSERA</span></router-link>
            <ul class="nav-bar">
                <ul class="sign-in">
                    <li class="sign-in__item"><router-link to="/login" class="sign-in__button">Log In</router-link></li>
                    <li class="sign-in__item"><router-link to="/register" class="sign-in__button">Register</router-link></li>
                </ul>
            </ul>
        </div>
        </nav>
        <section class="content">
            <router-view/>
        </section>
        <footer class="footer">
            <div class="container">
                <ul class="footer-links">
                    <li class="footer-links__item">
                        <a href="https://github.com/sora-yuka/graduate-project" target="_blank">
                            <img src="./components/source/social-links/github.png" alt="github.png">
                        </a>
                    </li>
                    <li class="footer-links__item">
                        <a href="#!" target="_blank">
                            <img src="./components/source/social-links/instagram.png" alt="instagram.png">
                        </a>
                    </li>
                    <li class="footer-links__item">
                        <a href="#!" target="_blank">
                            <img src="./components/source/social-links/linkedin.png" alt="linked-in.png">
                        </a>
                    </li>
                    <li class="footer-links__item">
                        <a href="#!" target="_blank">
                            <img src="./components/source/social-links/vk.png" alt="vk.png">
                        </a>
                    </li>
                </ul>
                <p class="policy">@2024. Дипломный проект Сабыркулов Н.Н.</p>
            </div>
        </footer>
    </div>
</template>

<style>
@import "./components/css/main.css";
</style>