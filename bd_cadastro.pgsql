-- create table alunos(
--     id serial PRIMARY key,
--     nome varchar(150) not null,
--     sexo varchar not null,
--     email varchar(100) not null,
--     img_url varchar,
--     contato varchar(20),
--     descricao varchar,
--     ativo boolean default true,
--     data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
-- )


-- INSERT INTO alunos (nome,sexo,email,img_url,contato,descricao) values('Gertrudes Goveiá', 'feminino','gertrudes@gmail.com', 'https://bit.ly/3yrYhZ9','31988557424','Charme e elegancia é o que me define');

-- INSERT INTO alunos (nome,sexo,email,img_url,contato,descricao) values('Magda Serrando', 'feminino','magda@gmail.com', 'https://bit.ly/3hjx83i','31988557424','Inteligencia e destreza são o meu ponto forte.');

-- insert into alunos (nome,sexo,email,img_url,contato,descricao) values('Astolfo da silva','Masculino','Astolfo@gmail.com','https://image.freepik.com/vetores-gratis/perfil-de-avatar-de-homem-no-icone-redondo_24640-14044.jpg%27,%2799451-4287', 'Sobre mim');

-- insert into alunos (nome,sexo,email,img_url,contato,descricao) values('Raimundo Rosa','Masculino','Raimundo_rosa@gmail.com','https://image.freepik.com/vetores-gratis/perfil-de-avatar-de-homem-no-icone-redondo_24640-14046.jpg%27,%2796534-2134', 'Sobre mim');

select * from  alunos;

-- UPDATE alunos SET sexo = 'Feminino' WHERE sexo = 'feminino';