// Service worker minimo: nao faz cache de nada. Existe so para satisfazer o
// criterio de instalabilidade do Chrome/Android (precisa de um SW com
// listener de fetch registrado, mesmo que ele nao faca nada).
self.addEventListener('fetch', function () {});
