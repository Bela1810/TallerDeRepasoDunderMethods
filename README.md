# ACTIVIDAD PARTICIPACIÓN 7

En esta actividad se implementarán las funcionalidades de los dundermethods.

Para los siguientes puntos debe utilizar pistas de tipos donde sea posible

1. Defina una clase Elemento usando el decorador @dataclass que contenga lo siguiente:
Un atributo nombre de tipo str
Un método especial para soportar la operación de igualdad == que permita comparar dos objetos de la clase Elemento indicando si el nombre es igual.

2. Defina una clase Conjunto que contenga lo siguiente:
Un atributo de instancia que representa la lista de objetos de la clase Elemento, inicialice el atributo como una lista vacía.
Un atributo de instancia nombre que contiene el nombre del conjunto. Inicialice dicho atributo a partir de un parámetro dado en el método inicializador.
Un atributo de clase contador que lleve registro del número de instancias creadas. Incremente en uno el valor de dicho atributo en el método inicializador.
Un atributo “privado” __id al cual se le asigna el valor actual del atributo de clase contador al momento de la inicialización. Defina una propiedad de solo lectura para dicho atributo (aquí deberá consultar cómo se define una propiedad de solo lectura en Python).
Un método de instancia contiene, el cual recibe como parámetro un objeto de la clase Elemento y retorna un valor bool indicando si el conjunto contiene ya un elemento con el mismo nombre.
Un método de instancia agregar_elemento, el cual recibe un objeto de la clase Elemento como parámetro y lo agrega a la lista de elementos si no está contenido ya en el conjunto (utilice el método anterior para verificar)
Un método unir que recibe otro conjunto como parámetro y agrega sus elementos a la lista de elementos del objeto actual en el que se invoca el método. Tenga en cuenta que un conjunto no puede tener elementos repetidos. Implemente también esta operación por medio de un método especial para soportar el operador +.
Un método de clase intersectar que recibe dos conjuntos como parámetros y retorna un nuevo conjunto con los elementos de la intersección de los conjuntos dados. Recuerde que la intersección de dos conjuntos está conformada por los elementos que pertenecen a ambos conjuntos. El nombre del conjunto resultante debe ser "<Nombre Conjunto 1> INTERSECTADO <Nombre Conjunto 2>.
Un método __str__ que retorne una representación legible de un conjunto con el siguiente formato
"Conjunto <nombre>: (<nombre elemento 1>, <nombre elemento 2>,...,<nombre elemento n>)"
