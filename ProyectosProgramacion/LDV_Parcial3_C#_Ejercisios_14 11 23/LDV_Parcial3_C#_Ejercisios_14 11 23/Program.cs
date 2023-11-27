using System;
using System.ComponentModel;
using System.Runtime.InteropServices;
using System.Text.RegularExpressions;

namespace Ejersicios
{
    class Program
    {
        static string SimplifyString(string myVar)
        {
            myVar = myVar.Replace(" ", "");
            myVar = myVar.Replace(",", "");
            myVar = myVar.Replace(".", "");
            myVar = myVar.ToLower();
            return myVar;
        }
        static bool CheckVarTypeToNumber(string myVar)
        {
            return float.TryParse(myVar, out _);
        }
        static bool CheckVarTypeToNormalString(string myVar)
        {
            Regex patron = new Regex("[^a-zA-Z]");
            return !patron.IsMatch(myVar);
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
        static float FloatInput(string inpt)
        {
            int res = 0;
            while (true)
            {
                Console.WriteLine("-- Escriba el numero para iniciar --");
                inpt = Console.ReadLine() ?? "";
                if (CheckVarTypeToNumber(inpt) == true)
                {
                    res = ConvertToInt(inpt);
                    break;
                }
                else
                {
                    Console.WriteLine("-- Asegurese de escribir un numero y revise la ortografia");
                }
            }
            return res;
        }
        static void Main()
        {
            string pInpt = "";
            float val1f;
            float val2f;
            float val3f;
            string val1s;
            bool val1b = false;
            bool val2b;
            char val1c;
            Console.WriteLine("--- Estos son los ejercisios del profe que ya hicimos bueno en fin lo que sea coman caca todos popo agua equis de ajajajaja ---");
            Console.WriteLine("--- Ejercisio 1 ---");
            Console.WriteLine("-- Hola usuario --");
            while (true) {
                Console.WriteLine("-- Por favor escriba su peso en kilogramos --");
                pInpt = Console.ReadLine() ?? "";
                if (CheckVarTypeToNumber(pInpt) == true)
                {
                    val1f = ConvertToInt(pInpt);
                    break;
                } else
                {
                    Console.WriteLine("-- Asegurese de escribir un numero y revise la ortografia");
                }
            }
            while (true)
            {
                Console.WriteLine("-- Por favor escriba su altura en metros --");
                pInpt = Console.ReadLine() ?? "";
                if (CheckVarTypeToNumber(pInpt) == true)
                {
                    val2f = ConvertToInt(pInpt);
                    break;
                }
                else
                {
                    Console.WriteLine("-- Asegurese de escribir un numero y revise la ortografia");
                }
            }
            // Se crean variables Double para poder hacer la operacion a potencias
            Double _val2 = (Double)val2f;
            Double superRes = 0;
            try
            {
                superRes = Math.Pow(val1f, 0.5f);
                val2f = (float)superRes;
            }
            catch
            {
                Console.WriteLine("!!! Algo salio mal !!!");
                val2f = 0;
            }
            val3f = val1f / val2f;
            Console.WriteLine("-- Tu indice de masa corporal es " + val3f);

            Console.WriteLine("--- Ejercisio 2 ---");
            Console.WriteLine("-- Tenemos 2 Grupos, Los de A y los del B --");
            Console.WriteLine("-- Los grupos estan divididos entre sexos y la primer letra de su nombre organizada alfabeticamente --");
            Console.WriteLine("-- El A conforme de Mujeres antes de la M y Hombres posterior a la N --");
            Console.WriteLine("-- El B conforme del resto de alumnos --");
            Console.WriteLine("-- Ingrese su nombre y su sexualidad y se le asignara un grupo --");
            while (true)
            {
                Console.WriteLine("-- Escriba M o F para asignar su sexualidad --");
                pInpt = Console.ReadLine() ?? "";
                pInpt = SimplifyString(pInpt);
                if (pInpt == "m" || pInpt == "f")
                {
                    if (pInpt == "m")
                    {
                        val1b = true;
                    }
                    if (pInpt == "f")
                    {
                        val1b = false;
                    }
                    break;
                }
                else
                {
                    Console.WriteLine("-- Asegurese de escribir solo letras y revise la ortografia");
                }
            }
            while (true)
            {
                Console.WriteLine("-- Escriba su nombre --");
                pInpt = Console.ReadLine() ?? "";
                pInpt = SimplifyString(pInpt);
                val1c = pInpt[0];
                val1s = val1c.ToString();
                if (CheckVarTypeToNormalString(val1s))
                {
                    if (val1b == true && val1c >= 'a' && val1c < 'm')
                    {
                        val2b = true;
                    } else if (val1b == false && val1c >= 'n' && val1c < 'z')
                    {
                        val2b = true;
                    }
                    else
                    {
                        val2b = false;
                    }
                    break;
                }
                else
                {
                    Console.WriteLine("-- Asegurese de escribir solo letras y revise la ortografia");
                }
            }
            if (val2b == true)
            {
                Console.WriteLine("-- Eres parte del grupo A --");
            } else {
                Console.WriteLine("-- Eres parte del grupo B --");
            }

            Console.WriteLine("--- Ejercisio 3 ---");
            val1f = 0;
            val2f = 0;
            val3f = 1;
            Console.WriteLine("-- Voy a escribir la serie fibonacci hasta el numero que me indiques --");
            val1f = FloatInput(val1s);
            for (int i = 0; val2f <= val1f; i++)
            {
                Console.Write("- " + val2f + " -");
                float temp = val2f;
                val2f = val3f;
                val3f = temp + val3f;
            }
            Console.WriteLine();

            Console.WriteLine("--- Ejercisio 4 ---");
            val1f = 0;
            val2f = 0;
            val3f = 0;
            Console.WriteLine("-- Dame un nunero para encontrar los numeros pares e impares para llegar a ese numero desde el 0 --");
            val1f = FloatInput(val1s);
            Console.WriteLine("-- Primero los numeros pares --");
            int parInt = 2;
            Console.WriteLine(parInt);
            while (parInt < val1f)
            {
                parInt += 2;
                Console.WriteLine("- " + parInt + " -");
            }
            Console.WriteLine("-- Ahora los numeros impares --");
            int oddInt = 1;
            Console.WriteLine(oddInt);
            while (oddInt < val1f)
            {
                oddInt += 2;
                Console.WriteLine("- " + oddInt + " -");
            }

            Console.WriteLine("--- Ejercisio 5 ---");
            val1f = 0;
            val2f = 1;
            Console.WriteLine("-- Escribe un numero y crearé un triangulo escaleno de ese tamanio --");
            val1f = FloatInput(val1s);
            while (val1f > val2f)
            {
                for (int x = 0; x < val2f; x++)
                {
                    Console.Write("*");
                }
                Console.WriteLine();
                val2f++;
            }
            Console.WriteLine("--- Ejercisio 6 ---");
            Console.WriteLine("-- Te voy a mostrar todas las letras del abecedario excepto las que e estan en posiciones de multiplos de 3 porque si --");
            List<char> abcd = new List<char>();
            for (char letra = 'A'; letra <= 'Z'; letra++)
            {
                abcd.Add(letra);
            }

            for (int i = abcd.Count - 1; i >= 0; i--)
            {
                if ((i + 1) % 3 == 0)
                {
                    abcd.RemoveAt(i);
                }
            }
            foreach (char letra in abcd)
            {
                Console.Write(letra + " ");
            }

            Console.WriteLine("--- Ejercisio 7 ---");
            while (true)
            {
                Console.WriteLine("-- Dame una frase o palabra para asegurarme que sea un palindromo --");
                pInpt = Console.ReadLine() ?? "";
                pInpt = SimplifyString(pInpt);
                if (CheckVarTypeToNormalString(val1s))
                {
                    break;
                }
                else
                {
                    Console.WriteLine("-- Asegurese de escribir solo letras y revise la ortografia --");
                }
            }
            Console.WriteLine("-- Revisemos que sea un palindromo --");
            val1b = true;
            int longitud = pInpt.Length;

            for (int i = 0; i < longitud / 2; i++)
            {
                if (pInpt[i] != pInpt[longitud - 1 - i])
                {
                    val1b = false; break;
                }
            }
            if (val1b)
            {
                Console.WriteLine("-- Si es un palindromo --");
            } else
            {
                Console.WriteLine("-- No es un palindromo --");
            }

            Console.WriteLine("--- Ejercisio 8 ---");
            Console.WriteLine("-- Ahora vamos a almacenar los datos que necesite en un diccionario, escriba Exit para salir --");
            Dictionary<string, string> myData = new Dictionary<string, string>();
            while (true)
            {
                Console.Write("-- Ingrese el tipo de información (nombre, edad, sexo, teléfono, etc.), o escriba Exit para salir --");
                while (true)
                {
                    pInpt = Console.ReadLine() ?? "";
                    pInpt = SimplifyString(pInpt);
                    if (CheckVarTypeToNormalString(val1s))
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("-- Asegurese de escribir solo letras y revise la ortografia --");
                    }
                }
                if (pInpt == "exit")
                {
                    Console.WriteLine("-- Exit Detectado --");
                    Console.WriteLine("-- Su diccionario final: " + myData + " --");
                    break;
                }

                Console.Write("-- Ingrese el valor para " + pInpt +": --");
                val1s = Console.ReadLine() ?? "";

                myData[pInpt] = val1s;

                Console.WriteLine("-- Contenido del diccionario: --");

                foreach (var kvp in myData)
                {
                    Console.WriteLine("-- " + kvp.Key +" - "+ kvp.Value + " --");
                }
                Console.WriteLine();
            }
            Console.WriteLine("--- Gracias por utilizar el programa, hasta luego ---");
        }
    }
}

