import fastify from "fastify";
import cors from "@fastify/cors";


const server = fastify({ logger: true, });

server.register(cors, {
    origin: "*",
    methods: ["GET"],
});
server.get("/teams", async (request, reply) => {
    reply.type("application/json").code(200);
    return [{ id: 1, name: "ferrari" }, { id: 2, name: "mercedes" }];
})

server.listen({ port: 3333 }, () => {
    console.log("Server is running on port 3000");
})
