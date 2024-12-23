use clap::{Arg, Command}; // Библиотека для обработки аргументов
use rand::{distributions::Alphanumeric, thread_rng, Rng, seq::SliceRandom}; // Библиотека для псевдорандома

// функция добавления выбранного количества символов в строку
fn add_to_string(input: &str, num_chars: usize, char_set: &str) -> String {
    let mut rng = rand::thread_rng();
    let mut result = input.to_string();

    let char_vec: Vec<char> = char_set.chars().collect();

    for _ in 0..num_chars {
        let random_char = char_vec.choose(&mut rng).unwrap();
        result.push(*random_char);
    }

    result
}

fn main(){
    // Декларируем наборы символов
    let letters = String::from("abcdefghijklmnopqrstuvwxyz");
    let uletters = String::from("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
    let numbers = String::from("0123456789");
    let specials = String::from("!@#$%^&*()-_=+[]{}|;:',.<>?/~`");
    let mut custom = String::from("");

    // работа c cli
    let matches = Command::new("Passgen")
        .version("1.0")
        .author("IU5-35B")
        .about("Password generation")
        .arg( // длина пароля
            Arg::new("len")
                .short('l')
                .long("len")
                .takes_value(true)
                .default_value("12")
                .help("Set the password length"),
        )
        .arg( // минимальное количество букв в пароле
            Arg::new("let")
                .short('s')
                .long("let")
                .takes_value(true)
                .default_value("0")
                .help("Minimum number of letters in the password"),
        )
        .arg( // минимальное количество цифр в пароле
            Arg::new("num")
                .short('n')
                .long("num")
                .takes_value(true)
                .default_value("0")
                .help("Minimum number of numbers in the password"),
        )
        .arg(   // минимальное количество заглавных букв в пароле
            Arg::new("ulet")
                .short('u')
                .long("ulet")
                .takes_value(true)
                .default_value("0")
                .help("Minimum number of upper case letters in the password"),
        )
        .arg(  // отсуствие специальных символов в пароле
            Arg::new("symb")
                .short('i')
                .long("symb")
                .takes_value(true)
                .help("Include special symbols in the password"),
        )
        .arg(  // отсутствие специальных символов в пароле
            Arg::new("excl")
                .short('x')
                .long("excl")
                .takes_value(false)
                .help("Exclude special symbols from the password"),
        )
        .arg(  // число сгенерированных паролей
            Arg::new("count")
                .short('c')
                .long("count")
                .takes_value(true)
                .default_value("1")
                .help("Generate multiple passwords"),
        )
        .get_matches();

    let length: usize = matches
        .get_one::<String>("len")
        .unwrap()
        .parse()
        .expect("Length must be a number");
    
    let slength: usize = matches
        .get_one::<String>("let")
        .unwrap()
        .parse()
        .expect("Length must be a number");

    let nlength: usize = matches
        .get_one::<String>("num")
        .unwrap()
        .parse()
        .expect("Length must be a number");


    let uslength: usize = matches
        .get_one::<String>("ulet")
        .unwrap()
        .parse()
        .expect("Length must be a number");

    let count: usize = matches
        .get_one::<String>("count")
        .unwrap()
        .parse()
        .expect("Count must be a number");

    let mut genpass = String::new();
    
    //цикл для генерации сразу нескольких паролей за раз
    let mut i = 0; 
    while i < count { 
        let mut genpass = String::new(); // Инициализируем новую строку для каждого пароля

        // Добавление символов в порядке, гарантируя минимальное количество каждого типа
        genpass = add_to_string(&genpass, slength, &letters); // Добавляем буквы нижнего регистра
        genpass = add_to_string(&genpass, nlength, &numbers); // Добавляем цифры
        genpass = add_to_string(&genpass, uslength, &uletters); // Добавляем буквы верхнего регистра

        // Для символов: добавляем оставшуюся часть, если включены символы
        let mut symbols = letters.clone() + &uletters + &numbers;
            
        if !matches.is_present("excl") {
            symbols += &specials; // Добавляем специальные символы, если не исключены
        }

        // Если общее количество символов меньше нужной длины, заполняем оставшиеся места случайными символами
        if genpass.len() < length {
            let remaining_length = length - genpass.len();
            genpass = add_to_string(&genpass, remaining_length, &symbols);
        }

        // Перемешиваем строку для случайного порядка символов
        let mut rng = thread_rng();
        let mut genpass_vec: Vec<char> = genpass.chars().collect();
        genpass_vec.shuffle(&mut rng);
        genpass = genpass_vec.iter().collect();

        println!("Вариант №{}: {}", i + 1, genpass);
        i += 1;
    }
}
