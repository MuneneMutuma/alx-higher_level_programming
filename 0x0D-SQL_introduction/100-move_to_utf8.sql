-- a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0
	DEFAULT CHARACTER SET utf8mb4;
ALTER TABLE first_table
	DEFAULT CHARACTER SET utf8mb4,
	MODIFY name VARCHAR(256)
		CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
