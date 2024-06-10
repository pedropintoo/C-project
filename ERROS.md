

## ERRORS

ex05_extra.agl: action on flame.state
hanoi.agl: visitAction não podemos obrigar isto:
// id type must be an EnumType 
      if (!idType.conformsTo(enumType)) {
         ErrorHandling.printError("Error: identifier \"" + id + "\" is not an enum type");
         return false;
      }

    : getConcrete...
    precisei de comentar isto:


- tentar perceber o visitLongAssignment.
Explica-me porque fazes isto:

if (type instanceof ObjectType) {
                  ObjectType objectType = new ObjectType(type.name());
O Rectangle devia entrar dentro do if pois é um tipo de Objeto mas não está a entrar
Como posso resolver isso?



-- Falta fazer validação do TIME -> só pode ser > 0.
