PGDMP     #    4                x            product_verification    12.1    12.1 :    Z           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            [           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            \           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ]           1262    24576    product_verification    DATABASE     �   CREATE DATABASE product_verification WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';
 $   DROP DATABASE product_verification;
                postgres    false            �            1259    24649    tbl_2stepverification    TABLE     �   CREATE TABLE public.tbl_2stepverification (
    ver_id integer NOT NULL,
    enabled character varying,
    account_id integer,
    code integer
);
 )   DROP TABLE public.tbl_2stepverification;
       public         heap    postgres    false            �            1259    24647     tbl_2stepverification_ver_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tbl_2stepverification_ver_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.tbl_2stepverification_ver_id_seq;
       public          postgres    false    213            ^           0    0     tbl_2stepverification_ver_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.tbl_2stepverification_ver_id_seq OWNED BY public.tbl_2stepverification.ver_id;
          public          postgres    false    212            �            1259    24622 	   tbl_login    TABLE     [  CREATE TABLE public.tbl_login (
    user_id integer NOT NULL,
    fullname character varying,
    email_address character varying,
    usename character varying,
    password character varying,
    profile_image character varying,
    status character varying,
    user_type character varying,
    acc_id bigint,
    ver_code character varying
);
    DROP TABLE public.tbl_login;
       public         heap    postgres    false            �            1259    24620    tbl_admin_login_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tbl_admin_login_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.tbl_admin_login_user_id_seq;
       public          postgres    false    209            _           0    0    tbl_admin_login_user_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.tbl_admin_login_user_id_seq OWNED BY public.tbl_login.user_id;
          public          postgres    false    208            �            1259    24590    tbl_city    TABLE     `   CREATE TABLE public.tbl_city (
    city_id integer NOT NULL,
    city_name character varying
);
    DROP TABLE public.tbl_city;
       public         heap    postgres    false            �            1259    24588    tbl_city_city_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tbl_city_city_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.tbl_city_city_id_seq;
       public          postgres    false    205            `           0    0    tbl_city_city_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.tbl_city_city_id_seq OWNED BY public.tbl_city.city_id;
          public          postgres    false    204            �            1259    24601    tbl_company    TABLE     r  CREATE TABLE public.tbl_company (
    comp_id integer NOT NULL,
    comp_name character varying,
    com_type_id integer,
    comp_logo character varying,
    comp_description character varying,
    city_id integer,
    comp_address character varying,
    comp_phone character varying,
    rep_phone character varying,
    status character varying,
    reg_date date
);
    DROP TABLE public.tbl_company;
       public         heap    postgres    false            �            1259    24599    tbl_company_comp_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tbl_company_comp_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.tbl_company_comp_id_seq;
       public          postgres    false    207            a           0    0    tbl_company_comp_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.tbl_company_comp_id_seq OWNED BY public.tbl_company.comp_id;
          public          postgres    false    206            �            1259    24579    tbl_company_type    TABLE     c   CREATE TABLE public.tbl_company_type (
    com_type_id integer NOT NULL,
    name text NOT NULL
);
 $   DROP TABLE public.tbl_company_type;
       public         heap    postgres    false            �            1259    24577     tbl_company_type_com_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tbl_company_type_com_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.tbl_company_type_com_type_id_seq;
       public          postgres    false    203            b           0    0     tbl_company_type_com_type_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.tbl_company_type_com_type_id_seq OWNED BY public.tbl_company_type.com_type_id;
          public          postgres    false    202            �            1259    24660    tbl_forget_pass    TABLE     �   CREATE TABLE public.tbl_forget_pass (
    for_id integer NOT NULL,
    account_id integer,
    reason character varying,
    token character varying,
    date timestamp without time zone
);
 #   DROP TABLE public.tbl_forget_pass;
       public         heap    postgres    false            �            1259    24658    tbl_forget_pass_for_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tbl_forget_pass_for_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.tbl_forget_pass_for_id_seq;
       public          postgres    false    215            c           0    0    tbl_forget_pass_for_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.tbl_forget_pass_for_id_seq OWNED BY public.tbl_forget_pass.for_id;
          public          postgres    false    214            �            1259    24633    tbl_product    TABLE     	  CREATE TABLE public.tbl_product (
    product_id integer NOT NULL,
    product_name character varying,
    comp_id integer,
    description character varying,
    man_date date,
    exp_date date,
    product_code character varying,
    status character varying
);
    DROP TABLE public.tbl_product;
       public         heap    postgres    false            �            1259    24631    tbl_product_product_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tbl_product_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.tbl_product_product_id_seq;
       public          postgres    false    211            d           0    0    tbl_product_product_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.tbl_product_product_id_seq OWNED BY public.tbl_product.product_id;
          public          postgres    false    210            �            1259    32807    view_company    VIEW     #  CREATE VIEW public.view_company AS
 SELECT tbl_company.comp_id,
    tbl_company.comp_name,
    tbl_company.comp_logo,
    tbl_company.comp_description,
    tbl_company.comp_phone,
    tbl_company.comp_address,
    tbl_company.rep_phone,
    tbl_company.status,
    tbl_company.reg_date,
    tbl_city.city_id,
    tbl_city.city_name,
    tbl_company_type.com_type_id,
    tbl_company_type.name,
    tbl_login.user_id,
    tbl_login.fullname,
    tbl_login.email_address,
    tbl_login.usename,
    tbl_login.profile_image,
    tbl_login.user_type
   FROM public.tbl_company,
    public.tbl_city,
    public.tbl_company_type,
    public.tbl_login
  WHERE ((tbl_company.com_type_id = tbl_company_type.com_type_id) AND (tbl_company.city_id = tbl_city.city_id) AND (tbl_company.comp_id = tbl_login.acc_id));
    DROP VIEW public.view_company;
       public          postgres    false    209    207    203    203    209    207    205    209    209    209    209    209    205    207    207    207    207    207    207    207    207    207            �            1259    32803    view_product    VIEW     �  CREATE VIEW public.view_product AS
 SELECT tbl_product.product_id,
    tbl_company.comp_id,
    tbl_company.comp_name,
    tbl_product.product_name,
    tbl_product.description,
    tbl_product.man_date,
    tbl_product.exp_date,
    tbl_product.status,
    tbl_product.product_code
   FROM public.tbl_product,
    public.tbl_company
  WHERE (tbl_product.comp_id = tbl_company.comp_id);
    DROP VIEW public.view_product;
       public          postgres    false    211    207    207    211    211    211    211    211    211    211            �
           2604    24652    tbl_2stepverification ver_id    DEFAULT     �   ALTER TABLE ONLY public.tbl_2stepverification ALTER COLUMN ver_id SET DEFAULT nextval('public.tbl_2stepverification_ver_id_seq'::regclass);
 K   ALTER TABLE public.tbl_2stepverification ALTER COLUMN ver_id DROP DEFAULT;
       public          postgres    false    212    213    213            �
           2604    24593    tbl_city city_id    DEFAULT     t   ALTER TABLE ONLY public.tbl_city ALTER COLUMN city_id SET DEFAULT nextval('public.tbl_city_city_id_seq'::regclass);
 ?   ALTER TABLE public.tbl_city ALTER COLUMN city_id DROP DEFAULT;
       public          postgres    false    205    204    205            �
           2604    24604    tbl_company comp_id    DEFAULT     z   ALTER TABLE ONLY public.tbl_company ALTER COLUMN comp_id SET DEFAULT nextval('public.tbl_company_comp_id_seq'::regclass);
 B   ALTER TABLE public.tbl_company ALTER COLUMN comp_id DROP DEFAULT;
       public          postgres    false    207    206    207            �
           2604    24582    tbl_company_type com_type_id    DEFAULT     �   ALTER TABLE ONLY public.tbl_company_type ALTER COLUMN com_type_id SET DEFAULT nextval('public.tbl_company_type_com_type_id_seq'::regclass);
 K   ALTER TABLE public.tbl_company_type ALTER COLUMN com_type_id DROP DEFAULT;
       public          postgres    false    203    202    203            �
           2604    24663    tbl_forget_pass for_id    DEFAULT     �   ALTER TABLE ONLY public.tbl_forget_pass ALTER COLUMN for_id SET DEFAULT nextval('public.tbl_forget_pass_for_id_seq'::regclass);
 E   ALTER TABLE public.tbl_forget_pass ALTER COLUMN for_id DROP DEFAULT;
       public          postgres    false    214    215    215            �
           2604    24625    tbl_login user_id    DEFAULT     |   ALTER TABLE ONLY public.tbl_login ALTER COLUMN user_id SET DEFAULT nextval('public.tbl_admin_login_user_id_seq'::regclass);
 @   ALTER TABLE public.tbl_login ALTER COLUMN user_id DROP DEFAULT;
       public          postgres    false    208    209    209            �
           2604    24636    tbl_product product_id    DEFAULT     �   ALTER TABLE ONLY public.tbl_product ALTER COLUMN product_id SET DEFAULT nextval('public.tbl_product_product_id_seq'::regclass);
 E   ALTER TABLE public.tbl_product ALTER COLUMN product_id DROP DEFAULT;
       public          postgres    false    211    210    211            U          0    24649    tbl_2stepverification 
   TABLE DATA           R   COPY public.tbl_2stepverification (ver_id, enabled, account_id, code) FROM stdin;
    public          postgres    false    213   K       M          0    24590    tbl_city 
   TABLE DATA           6   COPY public.tbl_city (city_id, city_name) FROM stdin;
    public          postgres    false    205   !K       O          0    24601    tbl_company 
   TABLE DATA           �   COPY public.tbl_company (comp_id, comp_name, com_type_id, comp_logo, comp_description, city_id, comp_address, comp_phone, rep_phone, status, reg_date) FROM stdin;
    public          postgres    false    207   SK       K          0    24579    tbl_company_type 
   TABLE DATA           =   COPY public.tbl_company_type (com_type_id, name) FROM stdin;
    public          postgres    false    203   &L       W          0    24660    tbl_forget_pass 
   TABLE DATA           R   COPY public.tbl_forget_pass (for_id, account_id, reason, token, date) FROM stdin;
    public          postgres    false    215   JL       Q          0    24622 	   tbl_login 
   TABLE DATA           �   COPY public.tbl_login (user_id, fullname, email_address, usename, password, profile_image, status, user_type, acc_id, ver_code) FROM stdin;
    public          postgres    false    209   gL       S          0    24633    tbl_product 
   TABLE DATA              COPY public.tbl_product (product_id, product_name, comp_id, description, man_date, exp_date, product_code, status) FROM stdin;
    public          postgres    false    211   �L       e           0    0     tbl_2stepverification_ver_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.tbl_2stepverification_ver_id_seq', 1, false);
          public          postgres    false    212            f           0    0    tbl_admin_login_user_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.tbl_admin_login_user_id_seq', 22, true);
          public          postgres    false    208            g           0    0    tbl_city_city_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.tbl_city_city_id_seq', 6, true);
          public          postgres    false    204            h           0    0    tbl_company_comp_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.tbl_company_comp_id_seq', 5, true);
          public          postgres    false    206            i           0    0     tbl_company_type_com_type_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.tbl_company_type_com_type_id_seq', 6, true);
          public          postgres    false    202            j           0    0    tbl_forget_pass_for_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.tbl_forget_pass_for_id_seq', 1, false);
          public          postgres    false    214            k           0    0    tbl_product_product_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.tbl_product_product_id_seq', 33, true);
          public          postgres    false    210            �
           2606    24657 0   tbl_2stepverification tbl_2stepverification_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.tbl_2stepverification
    ADD CONSTRAINT tbl_2stepverification_pkey PRIMARY KEY (ver_id);
 Z   ALTER TABLE ONLY public.tbl_2stepverification DROP CONSTRAINT tbl_2stepverification_pkey;
       public            postgres    false    213            �
           2606    24630    tbl_login tbl_admin_login_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.tbl_login
    ADD CONSTRAINT tbl_admin_login_pkey PRIMARY KEY (user_id);
 H   ALTER TABLE ONLY public.tbl_login DROP CONSTRAINT tbl_admin_login_pkey;
       public            postgres    false    209            �
           2606    24598    tbl_city tbl_city_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.tbl_city
    ADD CONSTRAINT tbl_city_pkey PRIMARY KEY (city_id);
 @   ALTER TABLE ONLY public.tbl_city DROP CONSTRAINT tbl_city_pkey;
       public            postgres    false    205            �
           2606    24609    tbl_company tbl_company_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.tbl_company
    ADD CONSTRAINT tbl_company_pkey PRIMARY KEY (comp_id);
 F   ALTER TABLE ONLY public.tbl_company DROP CONSTRAINT tbl_company_pkey;
       public            postgres    false    207            �
           2606    24587 &   tbl_company_type tbl_company_type_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public.tbl_company_type
    ADD CONSTRAINT tbl_company_type_pkey PRIMARY KEY (com_type_id);
 P   ALTER TABLE ONLY public.tbl_company_type DROP CONSTRAINT tbl_company_type_pkey;
       public            postgres    false    203            �
           2606    24668 $   tbl_forget_pass tbl_forget_pass_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.tbl_forget_pass
    ADD CONSTRAINT tbl_forget_pass_pkey PRIMARY KEY (for_id);
 N   ALTER TABLE ONLY public.tbl_forget_pass DROP CONSTRAINT tbl_forget_pass_pkey;
       public            postgres    false    215            �
           2606    24641    tbl_product tbl_product_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.tbl_product
    ADD CONSTRAINT tbl_product_pkey PRIMARY KEY (product_id);
 F   ALTER TABLE ONLY public.tbl_product DROP CONSTRAINT tbl_product_pkey;
       public            postgres    false    211            �
           2606    24615 $   tbl_company tbl_company_city_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tbl_company
    ADD CONSTRAINT tbl_company_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.tbl_city(city_id);
 N   ALTER TABLE ONLY public.tbl_company DROP CONSTRAINT tbl_company_city_id_fkey;
       public          postgres    false    205    2748    207            �
           2606    24610 (   tbl_company tbl_company_com_type_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tbl_company
    ADD CONSTRAINT tbl_company_com_type_id_fkey FOREIGN KEY (com_type_id) REFERENCES public.tbl_company_type(com_type_id);
 R   ALTER TABLE ONLY public.tbl_company DROP CONSTRAINT tbl_company_com_type_id_fkey;
       public          postgres    false    2746    203    207            �
           2606    24642 $   tbl_product tbl_product_comp_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tbl_product
    ADD CONSTRAINT tbl_product_comp_id_fkey FOREIGN KEY (comp_id) REFERENCES public.tbl_company(comp_id);
 N   ALTER TABLE ONLY public.tbl_product DROP CONSTRAINT tbl_product_comp_id_fkey;
       public          postgres    false    207    2750    211            U      x������ � �      M   "   x�3���/�H,�2���OOL�,�(����� iE      O   �   x�u�=s�0�g�Wh�F�!�+ǜ�-K�,��)6�\�]}�0��c��r���=��
���z�z?7i��:[�+��@���݃�]��U�*S�[/�v��m?� �:!�tEeG���4v*@��)��᳓�i�%���B<��
ye+������ �$t[��;���H!yo;$č��=�Yk�;c�'�M      K      x�3�I-.����� ��      W      x������ � �      Q   n   x����L�.MRp��MM�LL,L�4tH�M���K��� e9��9=}��M�--���99Sr3�8c������cc$S�� S�3K�
��A��y����\1z\\\ �I)�      S   �   x�U�Mn�0���sR�b�E�*�4�Ul����
[@���D����y���#(9��P��sD��w�� ��j��ܽ�F�)�959�[��
���Ba�Db����g������y9�d������`]Z�8�n���	��!�ئcg�z��V*��E��ʹ��<�l�ǘf�ad���^���1��T��vV�Մ�-.��,4�*�Djv�����᳌���q>���⦟T2��f{e^��vY���+q�     