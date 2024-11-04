from django.db import models

# Create your models here.
class Empresa(models.Model):
    codigo = models.CharField(max_length=10, default='')
    nome = models.CharField(max_length=255)
    razaosocial = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=15)
    inscricao_estadual = models.IntegerField(default=None, null=True)
    cidade = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=11, default='24342702')
    endereco_numero = models.CharField(default=11, max_length=10)
    complemento = models.CharField(max_length=100, default=None, null=True)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, default=None, null=True)

    def __str__(self):
        return"{}".format(self.nome)

class Almoxarifado (models.Model):
    codigo = models.CharField(max_length=3)
    descricao = models.CharField(max_length=255)
    Empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)


class Garagem (models.Model):
    descricao = models.CharField(max_length=255)
    Empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)


class TipoFornecedor (models.Model):
    descricao = models.CharField(max_length=255)


    def __str__(self):
        return "{}".format(self.descricao)



class Fornecedor (models.Model):
    codigo = models.CharField(max_length=10)
    razaosocial = models.CharField (max_length=255)
    nomefantasia = models.CharField(max_length=255)
    cnpj = models.CharField (max_length=20)
    inscricao_estadual = models.CharField (max_length=20, null=True, default=None)
    inscricao_municipal = models.CharField(max_length=20, null=True, default=None)
    nome_contato = models.CharField(max_length=50, null=True)
    telefone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    cep = models.CharField(max_length=255, null=True, default=None)
    bairro = models.CharField(max_length=255, null=True, default=None)
    cidade = models.CharField(max_length=255, null=True, default=None)
    uf = models.CharField(max_length=255, null=True, default=None)
    endereco = models.CharField(max_length=255, null=True, default=None)
    numero = models.CharField(max_length=255, null=True, default=None)
    complemento = models.CharField(max_length=255, null=True, default=None)
    observacao = models.CharField(max_length=255,null=True, default=None)
    observacao2 = models.CharField(max_length=255, null=True, default=None)
    categoria = models.ForeignKey (TipoFornecedor, on_delete=models.PROTECT, default=0)


    def __str__(self):
        return "{}".format(self.nomefantasia)



class Tanque (models.Model):
    descricao = models.CharField(max_length=255)
    garagem = models.ForeignKey(Garagem, on_delete=models.PROTECT)
    almoxarifado = models.ForeignKey(Almoxarifado, on_delete=models.PROTECT)

class Bomba (models.Model):
    descricao = models.CharField(max_length=255)
    tanque = models.ForeignKey(Tanque, on_delete=models.PROTECT)



class Carroceria (models.Model):

    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.marca} - {self.modelo}"


class Chassi(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.marca} - {self.modelo}"

class MotorTipo(models.Model):
    codigo = models.CharField(max_length=2)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao}"

class MotorMarca (models.Model):
    codigo = models.CharField(max_length=3)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao}"


class Carros (models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    placa = models.CharField(max_length=20,blank=True, null=True, default='')
    nr_chassis = models.CharField(max_length=25,blank=True, null=True, default='')
    chassi = models.ForeignKey(Chassi, on_delete=models.PROTECT)


    dt_aquis_chassis = models.DateField(blank=True, null=True, default='')
    ano_fabr_chassis = models.IntegerField(blank=True, null=True, default='')
    dt_ult_acum_chassis = models.DateField(blank=True, null=True, default='')
    chassi_km = models.DecimalField(max_digits=11, decimal_places=1,blank=True, null=True, default='')
    codigo_categoria_forn_ch = models.IntegerField(blank=True, null=True, default='')
    codigo_fornecedor_ch = models.CharField(max_length=10,blank=True, null=True, default='')
    nr_carroc = models.CharField(max_length=25,blank=True, null=True, default='')
    carroceria = models.ForeignKey(Carroceria, on_delete=models.PROTECT)

    dt_aquis_carroc = models.DateField(blank=True, null=True, default='')
    ano_fabr_carroc = models.IntegerField(blank=True, null=True, default='')
    dt_ult_acum_carroc = models.DateField(blank=True, null=True, default='')
    km_acum_carroc = models.DecimalField(max_digits=11, decimal_places=1, blank=True, null=True, default='')
    codigo_categoria_forn_ca = models.IntegerField(blank=True, null=True, default='')
    codigo_fornecedor_ca = models.CharField(max_length=10, blank=True, null=True, default='')
    tp_motor = models.CharField(max_length=3,blank=True, null=True, default=None)
    marca_motor = models.CharField(max_length=3, blank=True, null=True, default=None)
    motor_potencia = models.CharField(max_length=10,blank=True, null=True, default=None)
    codigo_classe_tp_combust = models.IntegerField(blank=True, null=True, default='')
    codigo_tipo_tp_combust = models.IntegerField(blank=True, null=True, default='')
    codigo_classe_tp_lubrif = models.IntegerField(blank=True, null=True, default='')
    codigo_tipo_tp_lubrif = models.IntegerField(blank=True, null=True, default='')
    codigo_medida_pneu_carro = models.CharField(max_length=7, blank=True, null=True, default='')
    qtde_pneus = models.IntegerField(blank=True, null=True, default='')
    nr_passag_sentados = models.IntegerField(blank=True, null=True, default='')
    nr_passag_empe = models.IntegerField(blank=True, null=True, default='')
    nr_placa = models.CharField(max_length=10, blank=True, null=True, default='')
    dt_entrada_operacao = models.DateField(blank=True, null=True, default='')
    dt_saida_operacao = models.DateField(blank=True, null=True, default='')
    codigo_tp_frota = models.IntegerField(blank=True, null=True, default='')
    codigo_tipo_veiculo = models.IntegerField(blank=True, null=True, default='')
    media_ideal_diesel = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default='')
    odometro_veiculo = models.DecimalField(max_digits=8, decimal_places=1, blank=True, null=True, default='')
    alienacao_veiculo = models.CharField(max_length=50, blank=True, null=True, default='')
    media_ideal_max_diesel = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default='')
    carro_ativo_veiculo = models.CharField(max_length=1, blank=True, null=True, default='')
    observacao_veiculo = models.CharField(max_length=200, blank=True, null=True, default='')
    nr_renavam_veiculo = models.CharField(max_length=20, blank=True, null=True, default='')
    codigo_tipo_tacografo = models.IntegerField(blank=True, null=True, default='')
    ano_modelo_chassis = models.IntegerField(blank=True, null=True, default='')
    ano_modelo_carroc = models.IntegerField(blank=True, null=True, default='')
    codigo_garagem = models.IntegerField(blank=True, null=True, default='')
    serie_motor = models.CharField(max_length=30, blank=True, null=True, default='')
    roleta_duplo_giro = models.CharField(max_length=1, blank=True, null=True, default='')
    planta_carroceria = models.IntegerField(blank=True, null=True, default='')
    equipe_manutencao = models.IntegerField(blank=True, null=True, default='')
    nr_serie_caixa = models.CharField(max_length=30, blank=True, null=True, default='')
    nr_serie_diferencial = models.CharField(max_length=30, blank=True, null=True, default='')
    ag_reguladora = models.CharField(max_length=15, blank=True, null=True, default='')
    cod_pintura_smtu = models.CharField(max_length=20, blank=True, null=True, default='')
    meta_diesel = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default='')
    codigo_carg = models.IntegerField(blank=True, null=True, default='')
    carro_reserva = models.CharField(max_length=1, blank=True, null=True, default='')
    tipo_servico = models.CharField(max_length=1, blank=True, null=True, default='')
    alias_carro = models.CharField(max_length=10, blank=True, null=True, default='')
    id_consorcio = models.IntegerField(blank=True, null=True, default=0)
    nr_lacre_placa = models.IntegerField(blank=True, null=True, default=0)
    alias_carro2 = models.CharField(max_length=10,blank=True, null=True, default='')
    condicao = models.CharField(max_length=1, default='A')
    nota_fiscal_chassi = models.CharField(max_length=20, blank=True, null=True, default='')
    nota_fiscal_carroc = models.CharField(max_length=20, blank=True, null=True, default='')
    capacidade_carter = models.IntegerField(blank=True, null=True, default=0)
    capacidade_tanque = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f"{self.codigo} - {self.nr_carroc}"


class Abastecimento (models.Model):
    a_emp = models.CharField(max_length=10, blank=True, null=True)
    data_abastecimento = models.DateField(default='1900-01-01')
    tipo = models.CharField(max_length=1)
    codigo_tanque = models.CharField(max_length=10, blank=True, null=True)
    codigo_bomba = models.CharField(max_length=10, blank=True, null=True)
    a_rta = models.CharField(max_length=10, blank=True, null=True)
    a_rbo = models.CharField(max_length=10, blank=True, null=True)
    carro = models.CharField(max_length=10)
    sequencia = models.IntegerField()
    diesel = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    a_rep = models.IntegerField(blank=True, null=True)
    a_cam = models.IntegerField(blank=True, null=True)
    a_hid = models.IntegerField(blank=True, null=True)
    a_fre = models.IntegerField(blank=True, null=True)
    a_dif = models.IntegerField(blank=True, null=True)
    a_gra = models.IntegerField(blank=True, null=True)
    odo_inicial = models.IntegerField()
    odo_final = models.IntegerField()
    a_hkm = models.IntegerField(default=1)
    a_sta = models.CharField(max_length=1, null=True, blank=True, default=None)
    a_hor = models.CharField(max_length=5, null=True, blank=True, default=None)
    a_mot = models.CharField(max_length=10,  null=True, blank=True, default=None)
    arla = models.DecimalField(max_digits=5, decimal_places=1, default=1.00)

    def __str__(self):
        return f"{self.carro} - {self.data_abastecimento}"

class PneMarca (models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.nome)

class PneMedida (models.Model):
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return"{}".format(self.descricao)

class PneTipo (models.Model):

    marca = models.ForeignKey(PneMarca, on_delete=models.PROTECT)
    descricao = models.CharField (max_length=255)

    def __str__(self):
        return "{}".format(self.descricao)

class PneMotivoSaida (models.Model):
    descricao = models.CharField(max_length=255)


    def __str__(self):
        return"{}".format(self.descricao)

class Grupos_Tipos(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return"{}".format(self.descricao)


class Grupos_Manutencao (models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.CharField(max_length=255)
    tipo = models.ForeignKey(Grupos_Tipos, on_delete=models.PROTECT, null=True, default=None)
    def __str__(self):
        return"{}".format(self.descricao)

class Grupo_Contabil (models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return"{}".format(self.descricao)

class Grupo_Estoque (models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return"{}".format(self.descricao)

class Tipo_Caracteristica (models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return"{}".format(self.descricao)

class Grupo_Compras (models.Model):
    codigo = models.CharField(max_length=4)
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return"{}".format(self.descricao)


class Almoxarifado_Material (models.Model):
    codigo = models.CharField(max_length=10)
    codigo_original = models.CharField(max_length=255, null=True, default=None)
    descricao = models.CharField(max_length=255)
    nome_praca = models.CharField(max_length=255, null=True, default=None)
    codigo_unidade_medida = models.CharField(max_length=5)
    utilizacao = models.CharField(max_length=255, null=True, default=None)
    codigo_fabricante = models.CharField(max_length=255, null=True, default=None)
    codigo_marca = models.CharField(max_length=255, null=True, default=None)
    codigo_tipo_condicao = models.CharField(max_length=4, null=True, default=None)
    codigo_grupo_contabil = models.CharField(max_length=4, null=True, default=None)
    codigo_grupo_estoque = models.CharField(max_length=4,  null=True, default=None )
    codigo_grupo_compras = models.CharField(max_length=4, null=True, default=None)
    flag_km = models.IntegerField(null=True, default=0)
    flag_integracao_contabil = models.IntegerField(null=True, default=0)
    codigo_natureza = models.IntegerField(null=True, default=0)

    def __str__(self):
        return"{}".format(self.descricao)




