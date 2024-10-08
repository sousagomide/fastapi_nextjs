"use client";

import { useContext, useEffect } from "react";
import { useRouter } from "next/navigation";
import AuthContext from "../context/AuthContext";

const ProtectedRoute = ({ children }) => {
    // o componente está usando o hook useContext para acessar o contexto de autenticação (AuthContext) e extrair a informação do usuário.
    const { user } = useContext(AuthContext);
    // Isso inicializa o objeto router do Next.js, que será usado para navegação programática.
    const router = useRouter();

    // O useEffect é usado para executar uma função de efeito que verifica se o usuário está autenticado.
    // O array de dependências [user, router] garante que o efeito será executado novamente se o usuário ou o router mudarem.
    useEffect(() => {
        if (!user) {
            router.push("/login");
        }
    }, [user, router]);

    //Se houver um usuário (autenticado), o componente renderiza os children
    return user ? children : null;
};

export default ProtectedRoute;
