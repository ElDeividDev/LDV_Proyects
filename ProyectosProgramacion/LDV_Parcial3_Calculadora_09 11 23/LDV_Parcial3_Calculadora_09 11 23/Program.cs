// Programa de Calculadora en C#

using System;

namespace Calculadora
{
    class Program
    {
        static float Calculate(float _value1, float _value2, int _type)
        {
            float res = 0;
            if (_type == 0) // Suma
            {
                res = _value1 + _value2;
            } else if (_type == 1) // Resta
            {
                res = _value1 - _value2;
            } else if (_type == 2) // Multiplicacion
            {
                res = _value1 * _value2;
            } else if (_type == 3) // Division
            {
                try
                {
                    // Checar si se puede hacer una division
                    res = _value1 / _value2;
                }
                catch
                {
                    Console.WriteLine("Se intento dividir entre 0");
                    res = 0;
                }
            } else if (_type == 4) // Potencia
            {
                // Se crean variables Double para poder hacer la operacion a potencias
                Double val1 = (Double)_value1;
                Double val2 = (Double)_value2;
                Double superRes = 0;
                try
                {
                    superRes = Math.Pow(val1, val2);
                    res = (float)superRes;
                } catch
                {
                    Console.WriteLine("Algo salio mal");
                    res = 0;
                }
            } else if (_type == 5) // Raiz
            {
                // Se crean variables Double para poder hacer la operacion a potencias
                Double val1 = (Double)_value1;
                Double val2 = (Double)_value2;
                Double superRes = 0;
                try
                {
                    val2 = 1 / val2;
                }
                catch
                {
                    Console.WriteLine("Se intentó dividir entre 0");
                    val2 = 0;
                }
                try
                {
                    superRes = Math.Pow(val1, val2);
                    res = (float)superRes;
                }
                catch
                {
                    Console.WriteLine("Algo salio mal");
                    res = 0;
                }
            }
            return res;
        }
        static bool CheckVarType(string myVar)
        {
            return float.TryParse(myVar, out _);
        }
        static float ConvertToFloat(string myVar)
        {
            float res;
            if (float.TryParse(myVar, out res))
            {
                return res;
            }
            return 0;
        }
        static int ConvertToInt(string myVar)
        {
            int res;
            if (int.TryParse(myVar, out res))
            {
                return res;
            }
            return -999;
        }
        static string SimplifyString(string myVar)
        {
            myVar = myVar.Replace(" ","");
            myVar = myVar.Replace(",","");
            myVar = myVar.Replace(".","");
            myVar = myVar.ToLower();
            return myVar;
        }
        static void Main()
        {
            //Console.WriteLine(Calculate(1, 1, 0));

            string pInpt = "";
            int opType = 0;
            float val1 = 0;
            float val2 = 0;
            float res = 0;
            bool closeProgram = false;
            // INTRODUCCION
            Console.WriteLine("--- Bienvenido a la mejor calculadora del mundo ---");
            Console.WriteLine("- Aqui puedes hacer operaciones con dos numeros -");

            while (true){
                while (true)
                {
                    Console.WriteLine("- Para hacer operaciones escriba; 0:Suma, 1:Resta, 2:Multiplicacion, 3:Division, 4:Potencia, 5:Raiz -");
                    Console.WriteLine("- Escriba 'Exit' para salir de la calculadora -");
                    pInpt = Console.ReadLine() ?? "";
                    pInpt = SimplifyString(pInpt);
                    if (pInpt == "exit") // Checa si escribo exit para salir
                    {
                        closeProgram = true;
                        break;
                    }
                    if (CheckVarType(pInpt) == true)
                    {
                        opType = ConvertToInt(pInpt); // Valor se vuelve numerico
                        if (opType < 6 && opType > -1)
                        {
                            Console.WriteLine("- Valor valido -");
                        } else
                        {
                            Console.WriteLine("- Escriba un valor dentro del rango permitido");
                            continue;
                        }
                        break;
                    }
                }
                if (closeProgram) { break; } // Checa si escribio exit para salir
                while (true)
                {
                    Console.WriteLine("- Escriba el PRIMER numero de su operacion");
                    pInpt = Console.ReadLine() ?? "";
                    if (CheckVarType(pInpt) == true)
                    {
                        val1 = ConvertToFloat(pInpt);
                        break;
                    }
                }
                while (true)
                {
                    Console.WriteLine("- Escriba el SEGUNDO numero de su operacion");
                    pInpt = Console.ReadLine() ?? "";
                    if (CheckVarType(pInpt) == true)
                    {
                        val2 = ConvertToFloat(pInpt);
                        break;
                    }
                }
                res = Calculate(val1, val2, opType);
                Console.WriteLine("- Su respuesta es: " + res + " -");
            }

            Console.WriteLine("--- Gracias por utilizr la calculadora, hasta luego :3 ---");
        }
    }
}
