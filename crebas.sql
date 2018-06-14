/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2018/6/14 15:43:52                           */
/*==============================================================*/


drop table if exists ACCOUNT;

drop table if exists ADMINISTRATOR;

drop table if exists Administrators;

drop table if exists BUSINESS_INFORMATION;

drop table if exists FUNCTION;

drop table if exists MSG_TEMPLATE;

drop table if exists ROLE_FUNCTION;

drop table if exists SEC_ROLE;

drop table if exists SMS;

drop table if exists SYSTEM_MESSAGE;

/*==============================================================*/
/* Table: ACCOUNT                                               */
/*==============================================================*/
create table ACCOUNT
(
   ID                   int(10) not null,
   ORDER_NUMBER         int(20),
   PAYMENT_ID           int(20),
   ACCOUNT_ID           int(20) not null,
   ACCOUNT_BOOK         int(4),
   AMOUNT               decimal,
   BALANCE              decimal,
   TYPE                 int(1) comment '0-充值，1-赠送',
   CREATE_DATE          datetime,
   PAYMENT_TYPE         int(1) comment '0-微信，1-支付宝，2-现金',
   primary key (ID)
);

alter table ACCOUNT comment '账户余额
#支付方式为页面要展现的，微商易仅支持支付宝';

/*==============================================================*/
/* Table: ADMINISTRATOR                                         */
/*==============================================================*/
create table ADMINISTRATOR
(
   ID                   int(10) not null auto_increment,
   PRODUCT_LINE_ID      int(10),
   FUNCTION_NAME        varchar(10),
   权限ID                 int(10) not null comment '权限包括什么产品线下的哪些角色权限',
   CREATE_DATE          datetime,
   ROLE_ID              int(10),
   primary key (ID)
);

alter table ADMINISTRATOR comment '待整理';

/*==============================================================*/
/* Table: Administrators                                        */
/*==============================================================*/
create table Administrators
(
   ID                   int(10) not null auto_increment,
   ADMINISTRATOR_ID     int(10) not null,
   PASSWORD             int(10),
   USER_NAME            int(20),
   FILE_ID              int(20),
   WECHAT_NUMBER        int(10),
   E_MAIL               int(10),
   SEX                  int(1),
   CREATE_DATE          datetime,
   IS_ADMIN             int(1) comment '是否为超级管理员',
   用户属性
   
   USER_ATTRIBUTE int(1),
   primary key (ID)
);

/*==============================================================*/
/* Table: BUSINESS_INFORMATION                                  */
/*==============================================================*/
create table BUSINESS_INFORMATION
(
   ID                   int(10) not null auto_increment,
   BUSINESS_NAME        varchar(50) not null,
   FILE_ID              varchar(50) not null,
   BUSINESS_ADDRESS     varchar(100) not null,
   CONTACTS_NAME        varchar(50) not null,
   CONTACTS_NUMBER      varchar(11),
   CREATE_DATE          datetime,
   primary key (ID)
);

/*==============================================================*/
/* Table: FUNCTION                                              */
/*==============================================================*/
create table FUNCTION
(
   ID                   int(10) not null auto_increment,
   FUNCTION_ID          int(10) not null,
   FUNCTION_NAME        varchar(30) not null,
   FUNCTION_LEVEL       int(1) not null,
   PARENT_FUNCTION_ID   int(10) not null,
   CREATE_DATE          datetime not null,
   primary key (ID, FUNCTION_ID)
);

alter table FUNCTION comment '权限关联';

/*==============================================================*/
/* Table: MSG_TEMPLATE                                          */
/*==============================================================*/
create table MSG_TEMPLATE
(
   ID                   int(10) not null auto_increment,
   TEMPLATE_ID          int(10) not null,
   TEMPLATE_NAME        varchar(20) comment '和短信表备注枚举相同',
   MESSAGE_CONTENT      varchar(80),
   CREATE_DATE          datetime,
   STATE                int(1),
   REMARKS              varchar(100),
   primary key (TEMPLATE_ID)
);

/*==============================================================*/
/* Table: ROLE_FUNCTION                                         */
/*==============================================================*/
create table ROLE_FUNCTION
(
   ID                   int(10) not null,
   ROLE_ID              int(10) not null,
   FUNCTION_ID          int(10) not null,
   CREATE_DATE          datetime,
   primary key (ID, ROLE_ID, FUNCTION_ID)
);

/*==============================================================*/
/* Table: SEC_ROLE                                              */
/*==============================================================*/
create table SEC_ROLE
(
   ID                   int(10) not null auto_increment,
   ROLE_NAME            int(20) not null,
   ROLE_ID              int(10) not null,
   NOTES                varchar(50) not null,
   STATE                int(1) not null,
   CREATE_DATE          datetime not null,
   primary key (ROLE_ID)
);

alter table SEC_ROLE comment '权限';

/*==============================================================*/
/* Table: SMS                                                   */
/*==============================================================*/
create table SMS
(
   ID                   int(10) not null auto_increment,
   PHONE_NUMBER         varchar(11),
   PRODUCT_LINE_ID      int(10),
   MESSAGE_AMOUNT       decimal,
   TYPE                 char(10) comment '枚举充值、赠送????',
   MESSAGE_TYPE         int(1) comment '枚举五个通知类型为短信模板的模板名称',
   STATE                int(1),
   CREATE_DATE          datetime,
   UPDATE_DATE          datetime,
   TEMPLATE_ID          int(10),
   primary key (ID)
);

/*==============================================================*/
/* Table: SYSTEM_MESSAGE                                        */
/*==============================================================*/
create table SYSTEM_MESSAGE
(
   ID                   int(10),
   PRODUCT_LINE_ID      int(10),
   MESSAGE_NAME         varchar(100),
   MESSAGE_CONTENT      varchar(100),
   CREATE_DATE          datetime,
   UPDATE_DATE          datetime
);

alter table ACCOUNT add constraint FK_Reference_16 foreign key (ID)
      references Administrators (ID) on delete restrict on update restrict;

alter table ADMINISTRATOR add constraint FK_Reference_13 foreign key (ID)
      references Administrators (ID) on delete restrict on update restrict;

alter table ADMINISTRATOR add constraint FK_Reference_17 foreign key (ROLE_ID)
      references SEC_ROLE (ROLE_ID) on delete restrict on update restrict;

alter table ROLE_FUNCTION add constraint FK_Reference_14 foreign key (ROLE_ID)
      references SEC_ROLE (ROLE_ID) on delete restrict on update restrict;

alter table ROLE_FUNCTION add constraint FK_Reference_15 foreign key (ID, FUNCTION_ID)
      references FUNCTION (ID, FUNCTION_ID) on delete restrict on update restrict;

alter table SMS add constraint FK_Reference_9 foreign key ()
      references MSG_TEMPLATE on delete restrict on update restrict;

