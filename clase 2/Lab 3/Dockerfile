# Etapa de construcción
FROM node:18 AS build
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build || echo "No build step"

# Etapa final (producción)
FROM node:18-alpine
WORKDIR /app
COPY --from=build /app/package.json .
COPY --from=build /app/ .
RUN npm install --only=production
COPY --from=build /app /app
EXPOSE 3000
CMD ["node", "index.js"]